#!/usr/bin/python3.6
#-*-coding: utf-8-*-

import ASCII

class paquet_loop2:

    def __init__(self, trame):
        print("Type LOOP2")
        self.m_trame = trame

    def get_type(self):
        return "LOOP2"

    def get_bar_trend(self):
        data = ASCII.getDecimal(self.m_trame[3])
        if data is "-60":
            return "Falling Rapidly"
        elif data is "-20":
            return "Falling Slowly"
        elif data is "0":
            return "Steady"
        elif data is "20":
            return "Rising Slowly"
        elif data is "60":
            return "Rising Rapidly"
        elif data is "80":
            return "P"

    def get_barometer(self):
        data1 = int(ASCII.getDecimal(self.m_trame[8]))
        data2 = int(ASCII.getDecimal(self.m_trame[7]))
        res = ((data1*256+data2)/1000)
        if (res > 20) and (res < 32.5):
            return res
        else:
            return None

    def get_inside_temperature(self):
        data1 = int(ASCII.getDecimal(self.m_trame[10]))
        data2 = int(ASCII.getDecimal(self.m_trame[9]))
        return self.__parse_fahrenheit_degres(data1, data2)

    def get_inside_humidity(self):
        return ASCII.getDecimal(self.m_trame[11])

    def get_outside_temperature(self):
        data1 = int(ASCII.getDecimal(self.m_trame[13]))
        data2 = int(ASCII.getDecimal(self.m_trame[12]))
        return self.__parse_fahrenheit_degres(data1, data2)

    def get_wind_speed(self):
        return int(ASCII.getDecimal(self.m_trame[14]))*1.60934

    def get_wind_direction(self):
        data1 = int(ASCII.getDecimal(self.m_trame[17]))
        data2 = int(ASCII.getDecimal(self.m_trame[16]))
        return self.__parse_fahrenheit_degres(data1, data2)

    def get_10min_avg_wind_speed(self):
        pass

    def get_2min_avg_wind_speed(self):
        pass

    def get_10min_wind_gust(self):
        pass

    def get_dew_point(self):
        pass

    def get_outside_humidity(self):
        pass

    def get_heat_index(self):
        pass

    def get_wind_chill(self):
        pass

    def get_thsw_index(self):
        pass

    def get_rain_rate(self):
        pass

    def get_uv(self):
        pass

    def get_solar_radation(self):
        pass

    def get_storm_rain(self):
        pass

    def get_start_date_of_current_storm(self):
        pass

    def get_daily_rain(self):
        pass

    def get_last_15min_rain(self):
        pass

    def get_last_hour(self):
        pass

    def get_daily_et(self):
        pass

    def get_last_24hour_rain(self):
        pass

    def get_barometric_reduction(self):
        pass

    def get_user_entered_barometric_offset(self):
        pass

    def get_barometric_calibration_number(self):
        pass

    def get_barometric_sensor_raw_reading(self):
        pass

    def get_absolute_barometric_pressure(self):
        pass

    def get_altimeter_setting(self):
        pass

    def get_next_wind_speed_graph_pointer(self, type):
        pass

    def get_next_minute_rain_graph(self):
        pass

    def get_next_rain_storm_graph_pointer(self):
        pass

    def get_index_minute_within(self):
        pass

    def get_next_rain(self, type):
        pass

    def __parse_fahrenheit_degres(self, data1, data2):
        res = ((data1 * 256 + data2) / 1000) * 33.86
        return res