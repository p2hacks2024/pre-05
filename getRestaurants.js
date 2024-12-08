const axios = require('axios');
const fs = require('fs');  // ファイルシステムモジュール
require('dotenv').config();  // dotenv を読み込んで環境変数を使えるようにする

// 環境変数からGoogle APIキーを取得
const GOOGLE_API_KEY = process.env.GOOGLE_MAP_API_KEY;

// 函館市の中心座標 (緯度, 経度)
const hakodateCenter = { lat: 41.768793, lng: 140.728810 };

// Google Places APIのURL
const googlePlacesUrl = 'https://maps.googleapis.com/maps/api/place/textsearch/json';

// 飲食店情報を取得する関数
async function fetchRestaurants(pageToken = '') {
  try {
    // APIリクエスト用のパラメータ
    const params = {
      query: 'restaurant',
      location: `${hakodateCenter.lat},${hakodateCenter.lng}`,
      radius: 15000, // 半径15km以内
      key: GOOGLE_API_KEY,  // 環境変数からAPIキーを使用
      pagetoken: pageToken,  // 次ページのデータを取得するためのトークン
    };

    // Google Places APIにリクエストを送信
    const response = await axios.get(googlePlacesUrl, { params });

    if (response.data.status === 'OK') {
      // 飲食店情報を取得
      const restaurants = response.data.results.map((place) => ({
        name: place.name,
        address: place.formatted_address,
        latitude: place.geometry.location.lat,
        longitude: place.geometry.location.lng,
        place_id: place.place_id,
      }));

      console.log('取得した飲食店情報:', restaurants);

      // 飲食店情報をJSONファイルとして保存
      saveRestaurantsToJsonFile(restaurants);

      // 次のページのデータがあれば、再帰的にfetchRestaurantsを呼び出す
      if (response.data.next_page_token) {
        console.log('次のページのデータを取得中...');
        fetchRestaurants(response.data.next_page_token);  // 再帰呼び出し
      }
    } else {
      console.error('APIリクエストエラー:', response.data.status);
    }
  } catch (error) {
    console.error('飲食店情報の取得エラー:', error);
  }
}

// 飲食店情報をJSONファイルとして保存する関数
function saveRestaurantsToJsonFile(restaurants) {
  const fileName = 'hakodate_restaurants.json';

  // 既存のファイルがあれば読み込み、新しいデータを追加
  if (fs.existsSync(fileName)) {
    const existingData = JSON.parse(fs.readFileSync(fileName, 'utf8'));
    restaurants = existingData.concat(restaurants);  // 既存データと新しいデータをマージ
  }

  // JSONデータをファイルに書き込む
  fs.writeFile(fileName, JSON.stringify(restaurants, null, 2), (err) => {
    if (err) {
      console.error('ファイル書き込みエラー:', err);
    } else {
      console.log(`${fileName} に飲食店情報を保存しました`);
    }
  });
}

// 飲食店情報を取得
fetchRestaurants();
