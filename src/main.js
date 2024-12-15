window.onload = function() {
  lucide.createIcons();
  const menuButton = document.querySelector('#menu-button');
  const popupMenu = document.querySelector('#popup-menu');
  const cityButtons = document.querySelectorAll('.city-button');

  menuButton.addEventListener('click', (e) => {
    e.preventDefault();
    popupMenu.classList.toggle('hidden');
  });

  // 點擊頁面其他位置時關閉選單（可選）
  document.addEventListener('click', (event) => {
    if (!menuButton.contains(event.target) &&
        !popupMenu.contains(event.target)) {
      popupMenu.classList.add('hidden');
    }
  });

  // 為每個城市按鈕添加點擊事件監聽器
  cityButtons.forEach(button => {
    button.addEventListener('click', async (e) => {
        e.preventDefault();  // 確保在事件處理開始就阻止預設行為
        e.stopPropagation(); // 阻止事件冒泡
        const cityName = button.value;
        await fetchWeatherInfo(cityName);
        popupMenu.classList.add('hidden');
        return false; // 額外防止表單提交
    });
  });

  // 定義取得並顯示天氣資訊的函式
  async function fetchWeatherInfo(cityName) {
    try {
        const apiUrl = `http://localhost:3000/weather?city=${encodeURIComponent(cityName)}`;
        $('#board').html('<p class="info">正在取得天氣資訊...</p>');

        const data = await $.post(apiUrl, 
            JSON.stringify({ city: cityName }), 
            null, 
            'json'
        );

        console.log('天氣資訊：', data);
        displayWeatherInfo(data);
        
    } catch (error) {
        console.error('資料獲取錯誤：', error);
        $('#board').html('<p class="error">無法取得天氣資訊。</p>');
    }
  }

  // 顯示天氣資訊的函式
  function displayWeatherInfo(location) {
    const weatherDesc =
        location.weatherElement.find(element => element.elementName === 'Wx')
            .time[0]
            .parameter.parameterName;
    const maxT =
        location.weatherElement.find(element => element.elementName === 'MaxT')
            .time[0]
            .parameter.parameterName;
    const minT =
        location.weatherElement.find(element => element.elementName === 'MinT')
            .time[0]
            .parameter.parameterName;
    const rainProb =
        location.weatherElement.find(element => element.elementName === 'PoP')
            .time[0]
            .parameter.parameterName;

    // <div class="weather-icon">${lucide.CloudRain}</div>
    document.querySelector('#board').innerHTML = `
            <div class="info">
            <h3>${location.locationName}</h3>
            <p>天氣狀況：${weatherDesc}</p>
            <p>最高溫度：${maxT}°C</p>
            <p>最低溫度：${minT}°C</p>
            <p>降雨機率：${rainProb}%</p>
            </div>
        `;
  }
}
