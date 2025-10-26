import platform

def get_platform_info():
    info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "architecture": platform.architecture(),
        "libc_version": platform.libc_ver(),
        "uname": platform.uname(),
    }
    return info