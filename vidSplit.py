import sys, subprocess, datetime, argparse, math

##accepts interval in seconds
##accepts video_path as .mp4 file
def time_split(video_path, interval, video_duration): 

    loop_num = math.ceil(video_duration/float(interval))
    
    video_duration = datetime.timedelta(seconds=video_duration) ##format video_duration 
    interval_delta = datetime.timedelta(seconds=interval) ##format interval
    i = 0 ##initialize iteration count
    
    while i < loop_num:
        position = datetime.timedelta(seconds=(interval*i))
        ##designate new file name
        new_file = video_path.replace('.mp4',(str(i)+'.mp4'))
        ##run video splitter
        command = 'ffmpeg -ss {0} -t {1} -i {2} -acodec copy -vcodec copy {3}'.format(position,interval_delta,video_path,new_file)
        subprocess.Popen([command], shell=True, stdout=subprocess.PIPE).stdout.read()
        
        i = i+1 ##update iteration counter
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the input')
    parser.add_argument('path', help='Enter a path')
    parser.add_argument('integers', type=int, nargs=2, help='Enter something')
    args = parser.parse_args()
    
    time_split(args.path, args.integers[0], args.integers[1])