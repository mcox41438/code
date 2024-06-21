import wmi
import sys
import ctypes

def is_write_filter_enabled():
    try:
        c = wmi.WMI()
        query = "SELECT * FROM Win32_SystemDriver WHERE Name Like '%ewf.sys' OR Name LIKE '%uwf.sys%'"
        result = c.query(query)

        for item in result:
            if "euf.sys" in item.Name.lower() or "uwf.sys" in item.Name.lower():
                return True
            
        return False
    
    except Exception as e:
        print(f"Failed to check Staus: {str(e)}")
        return False

def run_as_admin():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("me is admin")
            return True
        if not ctypes.windll.shell32.IsUserAnAdmin():
            try:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv),None, 1 )
                return True
            except Exception as e:
                print("I failed here")
                return False
            
    except Exception as e:
        print(f"Failed to elevate privilage: {str(e)}")
        return False
        
def setup_rename(new_name):
    c = wmi.WMI()

    for system in c.Win32_ComputerSystem():
        try:
            result = system.Rename(new_name)
            if result[0] == 0:
                print(f"Computer renamed to {new_name}")

            else:
                print(f"Computer failed to be renamed to {new_name}, error code: {result[0]}")
        except Exception as e:
            print(f"failed to rename computer: {str(e)}")


#add start button:
if is_write_filter_enabled:
    if run_as_admin():
        new_name= "Mason"
        setup_rename(new_name)
    else:
        print("can't do this shit")
else:
    print("goofy Goober")

