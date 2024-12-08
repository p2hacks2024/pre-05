const fs = require('fs');

const data = JSON.parse(fs.readFileSync('hakodate_restaurants.json', 'utf8'));
console.log('飲食店の件数:', data.length);
