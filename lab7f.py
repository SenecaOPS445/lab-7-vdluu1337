#!/usr/bin/env python3
# Student ID: 123964215

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        """Return a string representation for the object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Return the result by using sum_times() method."""
        sum = Time(0,0,0)
        sum.hour = self.hour + t2.hour
        sum.minute = self.minute + t2.minute
        sum.second = self.second + t2.second

        # Carry over if seconds exceed 59
        if sum.second >= 60:
            sum.minute += 1
            sum.second -= 60
        
        # Carry over if minutes exceed 59
        if sum.minute >= 60:
            sum.hour += 1
            sum.minute -= 60

        return sum

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """Check for the validity of the time object attributes."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

