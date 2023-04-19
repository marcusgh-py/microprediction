## PGA Tour streams


| Shorthand             | Example                                                                                                | Description                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Scores by greats players   | [tour_11_great.json](https://www.microprediction.org/stream_dashboard.html?stream=tour_11_great)          | Next net hole score by a great player on hole 11     |
| Scores by good players  | [tour_18_good.json](https://www.microprediction.org/stream_dashboard.html?stream=tour_18_good)     | Next net hole score by any good player on hole 18|
| Scores by okay players   | [tour_17_okay.json](https://www.microprediction.org/stream_dashboard.html?stream=tour_17_okay)      | Next net hole score by any okay player on hole 17 |
| Scores by bad players   | [tour_13_bad.json](https://www.microprediction.org/stream_dashboard.html?stream=tour_13_bad)      | Next net hole score by any bad player on hole 17 |
| Scores by any player   | [tour_7.json](https://www.microprediction.org/stream_dashboard.html?stream=tour_7)      | Next net hole score by any player on hole 7 |



### Definition of "good" etc

| Category | Skill Range                           | Description                                          |
|----------|---------------------------------------|------------------------------------------------------|
| great    | 1.34 ≤ skill ≤ 2.0                    | Player's skill is within 0.33 of 1.67                |
| good     | 0.67 ≤ skill ≤ 1.33                   | Player's skill is within 0.33 of 1.0                 |
| okay     | -0.25 ≤ skill ≤ 0.25                  | Player's skill is within 0.25 of 0.0                 |
| bad      | -1.33 ≤ skill ≤ -0.67                 | Player's skill is within 0.33 of -1.0                |


### Contender hole streams

See the updated contenders [names](https://micropredictionmiscstreams.pythonanywhere.com/contenders/names) and [scores](https://micropredictionmiscstreams.pythonanywhere.com/contenders/scores). For instance:

    from getjson import getjson
    contenders = getjson('https://micropredictionmiscstreams.pythonanywhere.com/contenders/name')
    
Once you know who the contenders are (fixed daily):    


| Shorthand             | Example                                                                                                | Description                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------|
|    | [pga_contender_1_hole_11.json](https://www.microprediction.org/stream_dashboard.html?stream=pga_contender_1_hole_11)          | The score on hole 11 by the 2nd listed condender    |








-+- 

Documentation [map](https://microprediction.github.io/microprediction/map.html)
 
  


