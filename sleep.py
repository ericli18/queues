import time

system_time = 0
ready_queue = []
sleep_queue = []


def start_process(name, sleep_duration):
    wakeup_time = system_time + sleep_duration
    print(
        f"   [syscall] {name} calls sleep({sleep_duration}). Wakes at tick {wakeup_time}."
    )
    sleep_queue.append((wakeup_time, name))
    sleep_queue.sort()


def run_os():
    global system_time # Use the global one (system time at the top of the script)
    print("--- OS Timer Started ---")

    start_process("Test program 1", 3)
    start_process("Test program 2", 8)
    start_process("Test program 3", 5)
    start_process("Test program 4", 3)

    while sleep_queue or ready_queue:
        print(f"\n--- Time {system_time} ---")

        while sleep_queue and sleep_queue[0][0] <= system_time:
            wake_time, proc_name = sleep_queue.pop(0)

            print(f"INTERRUPT: {proc_name}")
            ready_queue.append(proc_name)

        if ready_queue:
            proc = ready_queue.pop(0)
            print(f"CPU: Running {proc}")
        else:
            print("CPU: doing something else")

        time.sleep(0.5)
        system_time += 1

    print("\n--- Done ---")


if __name__ == "__main__":
    run_os()
