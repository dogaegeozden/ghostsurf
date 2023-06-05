main () {
    # The function which runs the entire script

    # Calling the drop_caches function.
    drop_caches

    # Calling the wipe_memory function
    wipe_memory
}

drop_caches() {
    # A function which drops caches

    echo 1024 > /proc/sys/vm/min_free_kbytes
    echo 3  > /proc/sys/vm/drop_caches
    echo 1  > /proc/sys/vm/oom_kill_allocating_task
    echo 1  > /proc/sys/vm/overcommit_memory
    echo 0  > /proc/sys/vm/oom_dump_tasks
}

wipe_memory() {
    # A function which wipes the memory securely

    # A function which wipes the memory securely
    sdmem -fllv
}

# Calling the main function
main