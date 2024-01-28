import psutil

class ProcessMonitor:
    def get_top_processes(self, limit=10):
        """
        Get top 'limit' processes sorted by CPU usage.

        :param limit: Number of processes to return. Default is 10.
        :return: List of top 'limit' processes sorted by CPU usage.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            processes.append(proc.info)

        # Sort by CPU usage and return the top 'limit' processes
        top_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:limit]
        return top_processes