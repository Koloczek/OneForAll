import speedtest

class bandwith:
    def run(self):
        speed = speedtest.Speedtest()

        download = round((speed.download()/1048576),2)
        upload = round((speed.upload()/1048576),2)
        print(f"Twoją prędkość pobierania wynosi: {download} Mb/s")
        print(f"Twoją prędkość wysyłania wynosi: {upload} Mb/s")

        input("Naciśnij Enter, aby kontynuować")