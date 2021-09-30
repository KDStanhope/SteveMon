## Purpose and objectives for the website/front-end portion of steve:
Show live sensor data
Show stats and graphs
    # Example:
        Show temp/rh/lux on a time period graph selectable (24h/48h/etc) with events as points. 
Show the preferences
    # Example:
        Setup:
            Attached Devices [light, light rail, heater, extractor, circulating fans, aircon, dehumidifier]
            Attached Sensors [{GrowSpace:[sensorID, data]},{Auxilliary Sensors:[SensorID, data]}]
        SteveMon settings: 
            Climate Control
            Lighting 
                Light Timer (on/off)
                    Time On (Time of day 24h) 
                    Duration (length HM)

                Light Intensity (on/off)
                    Time Pattern ***
            
                Light Rail (on/off)
                    Auto-Sync (on/off)
                OR
                    Time On (Time of day 24h) 
                    Duration (length HM) 

            Atmospheric
                Circulating Fans (on/off)
                    Time Pattern ***
            AND
                Heating (on/off)
                    Target Range
                        Target Temp (range 0 - 45)
                        Target Deviation (% deviation)
                        Duty Cycle (on/off)
                            Pulse Width (Hours:Minutes)
                            Time Period (Hours:Minutes)
            AND/OR
                Cooling (on/off)
                    Target Range 
                        Target Temp (range 0 - 45)
                        Target Deviation (% deviation)
                        Duty Cycle (on/off)
                            Pulse Width (Hours:Minutes)
                            Time Period (Hours:Minutes)
            AND/OR
                Extractor 
                    Timer (on/off)
                        Time Pattern ***
                AND/OR
                    Humidity Control Targeting (on/off)
                        Target Humidity (range 100 - 0)
                        Duty Cycle (on/off)
                                Pulse Width (Hours:Minutes)
                                Time Period (Hours:Minutes) 
                AND/OR
                    Differential Analysis (on/off) ####################### Could pull approx values from the internet if no exterior sensor!!!  
                        Target Temp (range 35-18)
                        Target Humidity (range 100-0)
                        Temperature/Humidity Bias (ratio as a %)
                        Extractor Priority (on/off)
                        Duty Cycle (on/off)
                                Pulse Width (Hours:Minutes)
                                Time Period (Hours:Minutes)
            OR
                VPD Targeting (on/of)
                    Target VPD (range 0.1-1.2)
                    Temperature/Humidity Bias (ratio as a %)
                    Enabled Devices [list of devices]
                    Differential Analysis (on/off) ####################### Could pull approx values from the internet if no exterior sensor!!!  
                    Extractor Priority (on/off)
                    Duty Cycle (on/off)
                                Pulse Width (Hours:Minutes)
                                Time Period (Hours:Minutes)



                                
                                








                



                
