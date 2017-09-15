import sys

class analog_clock(object):
    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute;
        #representation of the hour hand where every integer from 1-12 represents the number shown on an analog clock
        #and every 0.2 represents one of the single minute marks inbetween each hour mark.
        self.hour_hand = hour+((minute/12.0)*0.2)
        #representation of the minute hand where every integer from 1-12 represents the number shown on an analog clock
        # and every 0.2 represents one of the single minute marks inbetween each hour mark.
        self.minute_hand = float(int(self.minute/5)+((self.minute%5)*0.2))

def smallest_angle(clock):
    if(clock.minute_hand>clock.hour_hand):
        float_difference = min(clock.minute_hand-clock.hour_hand,(12-clock.minute_hand)+clock.hour_hand)
    else:
        float_difference = min(clock.hour_hand-clock.minute_hand,(12-clock.hour_hand)+clock.minute_hand)
    int_difference = int(float_difference)
    return round(int_difference*30 +((float_difference-int_difference)/0.2*6),1)

def main(argv):
    if len(argv)!=1:
        raise IOError("Wrong number of arguments.")
    try:
        f = open(argv[0],'r')
    except FileNotFoundError:
        print("Invalid File Name")
    time_arr = f.readlines()
    counter = 1
    for time in time_arr:
        digital = time.split(':')
        if(len(digital)!=2):
            raise IOError("Incorrect format")
        try:
         hour = int(digital[0])
         minute = int(digital[1])
        except ValueError:
            print("Error")
        if (hour<0 or hour>24 or minute<0 or minute>59):
            print("Error")
            break;
        if(hour>12):
            hour = hour-12
        new_clock = analog_clock(hour,minute)
        print ("Smallest Angle for Time "+str(counter)+" : "+str(smallest_angle(new_clock)))
        counter += 1


if __name__ == '__main__':
   main(sys.argv[1:])