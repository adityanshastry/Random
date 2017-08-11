import os
import subprocess
import time


def notify(title, message):
    notification_title = '-title {!r}'.format(title)
    notification_message = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([notification_title, notification_message])))


def notify_file_lines(files, check_files):

    line_counts = [0 for _ in xrange(len(files))]
    continue_notifications = True

    while continue_notifications:
        message = []
        for data_file_index, data_file in enumerate(files):
            line_count = int(subprocess.check_output(['wc', '-l', data_file]).strip().split()[0])
            if data_file_index+1 in check_files and line_count == line_counts[data_file_index]:
                continue_notifications = False
            else:
                line_counts[data_file_index] = line_count
                message.append(str(line_count))
        notify("Extraction Progress", ", ".join(message))

        time.sleep(60)


def main():
    notify_file_lines(["/Users/BatComp/Desktop/UMass/IESL/Code/watr-works/arxiv-sample_1.txt",
                       "/Users/BatComp/Desktop/UMass/IESL/Code/watr-works/arxiv-exceptions_2.txt"], [1])
    # notify("g", "qw")

if __name__ == '__main__':
    main()
