const fs = require('fs');

// JSONファイルの読み込み
const fileName = 'hakodate_restaurants.json';

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error('ファイル読み込みエラー:', err);
    return;
  }

  const restaurants = JSON.parse(data);

  // 店名のリストを作成
  const restaurantNames = restaurants.map(restaurant => restaurant.name);

  // 重複した店名を探す
  const duplicates = findDuplicates(restaurantNames);

  if (duplicates.length > 0) {
    console.log('重複した店名:', duplicates);
  } else {
    console.log('重複した店名はありません');
  }
});

// 重複を検出する関数
function findDuplicates(arr) {
  const seen = new Set();
  const duplicates = [];

  arr.forEach(item => {
    if (seen.has(item)) {
      duplicates.push(item);
    } else {
      seen.add(item);
    }
  });

  return duplicates;
}
