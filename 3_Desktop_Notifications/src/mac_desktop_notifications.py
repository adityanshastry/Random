import os
import subprocess
import time


def notify(title, message):
    notification_title = '-title {!r}'.format(title)
    notification_message = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([notification_title, notification_message])))


def notify_file_lines(files, check_files, monitor_time):

    line_counts = [0 for _ in xrange(len(files))]
    continue_notifications = True
    equal_count = 0

    while equal_count <= 2:
        message = []
        for data_file_index, data_file in enumerate(files):
            line_count = int(subprocess.check_output(['wc', '-l', data_file]).strip().split()[0])
            message.append(str(line_count))
            if data_file_index+1 in check_files and line_count == line_counts[data_file_index]:
                equal_count += 1
            else:
                line_counts[data_file_index] = line_count

        print message
        notify("Extraction Progress", ", ".join(message))

        time.sleep(monitor_time)


def main():
    notify_file_lines(["/Users/BatComp/Desktop/UMass/IESL/Code/watr-works/arxiv-sample_1.txt",
                       "/Users/BatComp/Desktop/UMass/IESL/Code/watr-works/arxiv-exceptions_2.txt"], [1], 60)


if __name__ == '__main__':
    main()
