dataAPI = {
  "coord": [
    "${json-unit.any-number}",
    "${json-unit.any-number}"
  ],
  "list": [
    {
      "dt": "${json-unit.any-number}",
      "main": {
        "aqi": "${json-unit.any-number}"
      },
      "components": {
        "co": "${json-unit.any-number}",
        "no": "${json-unit.any-number}",
        "no2": "${json-unit.any-number}",
        "o3": "${json-unit.any-number}",
        "so2": "${json-unit.any-number}",
        "pm2_5":"${json-unit.any-number}",
        "pm10": "${json-unit.any-number}",
        "nh3": "${json-unit.any-number}"
      }
    }
  ]
}