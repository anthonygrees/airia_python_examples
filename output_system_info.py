# outputs the system information for where the code block executes
#
import os
import platform
 
def get_system_info():
    # Get system information using os.uname()
    uname_info = os.uname()
    
    # Get kernel version using platform.release()
    kernel_version = platform.release()
 
    # Get user ID, group ID, process ID, and parent process ID
    user_id = os.getuid()
    group_id = os.getgid()
    process_id = os.getpid()
    parent_process_id = os.getppid()
 
    # Get CPU count
    cpu_count = os.cpu_count()
 
    # Get system load (1 min, 5 min, 15 min)
    system_load_1, system_load_5, system_load_15 = os.getloadavg()
 
    # Concatenate the information with carriage returns
    system_info = (
        f"System Name: {uname_info.sysname}\n"
        f"Node Name: {uname_info.nodename}\n"
        f"Release: {uname_info.release}\n"
        f"Version: {uname_info.version}\n"
        f"Machine: {uname_info.machine}\n"
        f"Kernel Version: {kernel_version}\n"
        f"User ID: {user_id}\n"
        f"Group ID: {group_id}\n"
        f"Process ID: {process_id}\n"
        f"Parent Process ID: {parent_process_id}\n"
        f"CPU Count: {cpu_count}\n"
        f"System Load (1 min): {system_load_1}\n"
        f"System Load (5 min): {system_load_5}\n"
        f"System Load (15 min): {system_load_15}"
    )
    
    return system_info
 
# Print the concatenated system information with carriage returns
output = (get_system_info())
 
