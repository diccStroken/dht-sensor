const attributeSelector = (name) => {
    return `[data-js="${name}"]`
};

const updateTimestamp = (timestamp) => {
    const timestampElement = document.querySelector(attributeSelector("timestamp"));

    timestampElement.innerHTML = timestamp;
};

const updateTemperature = (temperature) => {
    const temperatureElement = document.querySelector(attributeSelector("temperature-count"));

    temperatureElement.innerHTML = temperature;
};

const updateHumidity = (humidity) => {
    const humidityElement = document.querySelector(attributeSelector("humidity-count"));

    humidityElement.innerHTML = humidity;
};

const initializeCounter = () => {
    fetch("/api/dht/single")
    .then((response) => response.json())
    .then((responseJson) => {
        updateTimestamp(responseJson["timestamp"]);
        updateTemperature(responseJson["temperature"]);
        updateHumidity(responseJson["humidity"])

        console.log("fetching...")
    });
};

initializeCounter();
setInterval(initializeCounter, 5000);
