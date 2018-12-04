#!/usr/bin/python3.6
#-*-coding:utf-8-*-

class paquet_loop:

    dict_offset = {

    }

    def __init__(self, trame):
        print("Type LOOP")
        self.m_trame = trame

    def get_type(self):
        return "LOOP"

    def get_next_record(self):
        pass

    def get_barometer(self):
        pass

    def get_inside_temperature(self):
        pass

    def get_inside_humidity(self):
        pass

    def get_outside_temperature(self):
        pass

    def get_wind_speed(self):
        pass

    def get_10min_avg_wind_speed(self):
        pass

    def get_wind_direction(self):
        pass

    def get_extra_temperature(self):
        pass

    def get_soil_temperature(self):
        pass

    def leaf_temperature(self):
        pass

    def get_outside_temperature(self):
        pass

    def get_extra_humidity(self):
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

    def get_day_rain(self):
        pass

    def get_month_rain(self):
        pass

    def get_year_rain(self):
        pass

    def get_day_et(self):
        pass

    def get_month_et(self):
        pass

    def get_year_et(self):
        pass

    def get_soil_moistures(self):
        pass

    def get_leaf_wetnesses(self):
        pass

    def get_inside_alarms(self):
        pass

    def get_rain_alarms(self):
        pass

    def get_outside_alarms(self):
        pass

    def get_extra_temp_alarms(self):
        pass

    def get_soil_alarms(self):
        pass

    def get_console_battery_voltage(self):
        pass

    def get_time_of_sunrise(self):
        pass

    def get_time_of_sunset(self):
        pass

    def __parse_fahrenheit_degres(self, data1, data2):
        res = ((data1 * 256 + data2) / 1000) * 33.86
        return res