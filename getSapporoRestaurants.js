const axios = require('axios');
const fs = require('fs').promises;
require('dotenv').config();

const HOT_PEPPER_API_KEY = process.env.HOT_PEPPER_API_KEY;
const sapporoCenter = { lat: 43.062096, lng: 141.354376 }; // 札幌駅付近
const hotPepperUrl = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/';

async function fetchRestaurants() {
  try {
    const allRestaurants = new Map();
    let page = 1;
    let total = 0;

    while (true) {
      const params = {
        key: HOT_PEPPER_API_KEY,
        lat: sapporoCenter.lat,
        lng: sapporoCenter.lng,
        range: 3,
        format: 'json',
        start: (page - 1) * 100 + 1,
        count: 100
      };

      console.log(`APIリクエスト: ページ ${page}, 開始位置 ${params.start}`);
      const response = await axios.get(hotPepperUrl, { params });

      if (!response.data.results || !response.data.results.shop) {
        break;
      }

      const shops = response.data.results.shop;
      total = response.data.results.results_available;
      console.log(`取得した店舗数: ${shops.length}`);
      console.log(`総件数: ${total}`);

      shops.forEach(shop => {
        if (!allRestaurants.has(shop.id)) {
          allRestaurants.set(shop.id, {
            name: shop.name,
            address: shop.address,
            latitude: parseFloat(shop.lat),
            longitude: parseFloat(shop.lng),
            shop_id: shop.id
          });
        }
      });

      if (params.start + shops.length > total) {
        break;
      }

      page++;
    }

    const restaurants = Array.from(allRestaurants.values());
    await saveRestaurantsToJsonFile(restaurants);
    return restaurants;

  } catch (error) {
    console.error('APIエラー:', error.response?.data || error.message);
    throw error;
  }
}

async function saveRestaurantsToJsonFile(restaurants) {
  const fileName = 'sapporo_restaurants.json';
  try {
    await fs.writeFile(
      fileName,
      JSON.stringify(restaurants, null, 2)
    );
    console.log(`${fileName} に ${restaurants.length} 件の飲食店情報を保存しました`);
  } catch (err) {
    console.error('ファイル書き込みエラー:', err);
    throw err;
  }
}

fetchRestaurants()
  .catch(error => {
    console.error('処理エラー:', error);
    process.exit(1);
  });