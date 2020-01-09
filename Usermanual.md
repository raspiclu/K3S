## Stückliste

- Raspberry Pi 3 (6x)
- LAN-Kabel (6x)
- Switch (1x)
- Netzteil (2x)
- SD-Karte (6x)
- Tastatur (ggfs. selbst besorgen)
- Monitor bzw. Beamer mit HDMI-Anschluss (ggfs. selbst besorgen)

## Software
(nur notwendig, wenn die SD-Karten ohne Image zur Verfügung gestellt werden)
- [balenaEtcher](https://www.balena.io/etcher/)
- [SD Card Formatter](https://www.sdcard.org/downloads/formatter/)
- [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/)

## Vorbereitungen

1) Hardware prüfen:
- Sind alle Raspberry Pis mit dem Switch verbunden?
- Ist der Switch eingesteckt?
- Sind alle Raspberry Pis mit dem Netzteil verbunden?
- Ist das Netzteil eingesteckt?

2) Master-Raspberry Pi definieren:
Hinweis: Am besten wird der erste Raspberry Pi als master zur Cluster-Orchestrierung verwendet, so kann er von außen auf einen Blick erkannt werden.
- Bildschirm über HDMI Anschluss an den master-Raspberry anschließen
- Tastatur über USB Anschluss an den master-Raspberry anschließen

3) Images auf SD Karte flashen (nur notwendig, wenn SD-Karten ohne Image bereitgestellt werden):
- Image "Raspbian Lite" als Zip-Datei downloaden
- balenaEtcher öffnen und Zip-File einfügen
- Micro-SD-Karte über SD Kartenleser mit dem PC verbinden (ev. Adapter notwendig)
- balenaEtcher ausführen und das Betriebssystem auf die Micro-SD-Karte flashen
- Micro-SD-Karte in den Raspberry Pi einfügen

## DHCP-Server installieren
(wird nur am master-Raspberry Pi durchgeführt)

1) master-Raspberry starten:
- Stromkabel einstecken damit der Raspberry Pi hochfährt
- am master einloggen: <br>
User: *pi* <br>
Passwort: *raspberry*

1) Download des Tools: 
 `sudo apt-get install dnsmasq`

2) Öffnen der Konfigurationsdatei: 
`sudo nano /etc/dnsmasq.conf`

3) Eintragen der Einstellungen:
 
```
interface=eth0

# DHCP-Server nicht aktiv für bestehendes Netzwerk
no-dhcp-interface=wlan0

# IPv4-Adressbereich und Lease-Time
dhcp-range=10.10.1.10,10.10.1.200,600h

# DNS
dhcp-option=option:dns-server,192.168.137.1

# Alleiniger DHCP-Server
dhcp-authoritative
```

4) Testen der Einstellungen:
` dnsmasq --test -C /etc/dnsmasq.conf `

5) DNSMASQ neu starten:
`sudo systemctl restart dnsmasq`

6) DNSMASQ-Status anzeigen:
`sudo systemctl status dnsmasq`

7) DNSMASQ beim Systemstart starten:
`sudo systemctl enable dnsmasq`

8) Nodes hochfahren: 
- Stromkabel der übrigen Raspberry Pis ("Nodes") einstecken damit sie hochfahren

9) Auslesen der vergegebenen Leases:
`cat /var/lib/misc/dnsmasq.leases`

Wenn alle IP-Adressen erfolgreich vergeben wurden, werden nun alle Nodes des Clusters aufgeführt.

## Cluster-Aufbau
(einmalig am master-Raspberry durchführen um das Cluster einzurichten)

1) Git installieren:
´sudo apt-get install git´

2) Ansible installieren:
´sudo apt-get install ansible´

3) Repository angeben und Files runterladen:
´Git clone https://github.com/xxxxx´ (ACHTUNG, es muss noch ein Git-Repository angelegt werden!!)

4) Ansible Skripte ausführen

```
ansible-playbook -i hosts.ini capture_all_dhcp_leases.yml

ansible-playbook -i hosts.ini site.yml
```
## Cluster-Erweiterung
(nur ausführen, wenn neue Raspberry Pis hinzugefügt werden)

```
ansible-playbook -i oneHost.ini capture_dhcp_leases.yml

ansible-playbook -i oneHost.ini joinNew.yml
```
