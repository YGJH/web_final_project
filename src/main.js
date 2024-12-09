window.onload = function() {
    lucide.createIcons();

    const menuButton = document.getElementById('menu-button');
    const popupMenu = document.getElementById('popup-menu');

    menuButton.addEventListener('click', () => {
        popupMenu.classList.toggle('hidden');
    });

    // 點擊頁面其他位置時關閉選單（可選）
    document.addEventListener('click', (event) => {
        if (!menuButton.contains(event.target) && !popupMenu.contains(event.target)) {
            popupMenu.classList.add('hidden');
        }
    });

    const apiUrl = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-EBC821F3-9782-4630-8E87-87FF25933C15&format=JSON&sort=time';
    const selectedCityWeatherDiv = document.getElementById('selected-city-weather');
    let locations = [];

    // 取得天氣資料
    fetch(apiUrl)
        .then((response) => {return response.json()})
        .then(data => {
            console.log(data);
            locations = data.records.location;
            // 這裡可以移除先前填充下拉選單的代碼

            // 其他已有的程式碼

            // 取得所有城市按鈕
            const cityButtons = document.querySelectorAll('.city-button');

            // 為每個按鈕添加點擊事件監聽器
            cityButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const cityName = button.value;
                    // 調用顯示天氣資訊的函式
                    displayWeatherInfo(cityName, locations, selectedCityWeatherDiv);
                    // 關閉選單
                    popupMenu.classList.add('hidden');
                });
            });
        })
        .catch(error => console.error('資料獲取錯誤：', error));

    // 顯示天氣資訊的函式
    function displayWeatherInfo(cityName, locations, displayDiv) {
        const location = locations.find(loc => loc.locationName === cityName);
        if (location) {
            const weatherDesc = location.weatherElement.find(element => element.elementName === 'Wx').time[0].parameter.parameterName;
            const maxT = location.weatherElement.find(element => element.elementName === 'MaxT').time[0].parameter.parameterName;
            const minT = location.weatherElement.find(element => element.elementName === 'MinT').time[0].parameter.parameterName;
            const rainProb = location.weatherElement.find(element => element.elementName === 'PoP').time[0].parameter.parameterName;
            displayDiv.innerHTML = `
                <h3>${location.locationName}</h3>
                <p>天氣狀況：${weatherDesc}</p>
                <p>最高溫度：${maxT}°C</p>
                <p>最低溫度：${minT}°C</p>
                <p>降雨機率：${rainProb}%</p>
            `;
        } else {
            displayDiv.innerHTML = '<p>無法取得該地區的天氣資訊。</p>';
        }
    }
}