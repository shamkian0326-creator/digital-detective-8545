# Mission 7 — Trace a website request

## 1. Task / objective

Explain common network concepts, check an example website from Terminal and trace how a web page reaches the browser.

## 2. Work completed

Sent an HTTPS request to the public example domain `example.org` and looked up its IPv4 records. Saved the response code and public DNS addresses.

## 3. Commands / tools used

`curl --head` requested the response headers. Its status output showed that the web service responded. `dig +short example.org A` queried DNS and displayed the answer records for the domain.

## 4. My understanding

| Concept | What it means | Example |
| --- | --- | --- |
| LAN | Connects devices within a nearby site. | Computers sharing a printer in a lab. |
| MAN | Links networks over a city-sized area. | A network joining several buildings across a municipality. |
| WAN | Links networks across large regions. | An organization connecting offices in different countries. |
| DNS | Resolves names to records, such as IP addresses. | Looking up the address records for `example.org`. |
| Router | Sends packets onward between networks. | A router forwards home-network packets toward the internet provider. |
| Protocol | Specifies how systems format and exchange messages. | HTTP defines how clients request web resources. |
| Packet switching | Sends data as smaller units that can be forwarded independently over shared links. | Several page requests can travel through the same network at once. |
| Client-server | One program asks for a resource or service and another supplies it. | A browser asks a web server for a page. |

The connectivity test checks whether the client can reach the web service and receive a response. The DNS lookup displays the answers for the record type requested, which is IPv4 in this exercise. DNS helps the browser locate a server address when the user enters a domain name.

### What happens when the browser opens a website

1. The browser, acting as the client, reads the URL to determine which host and resource to request.
2. It finds an IP address in a cache or obtains one using DNS.
3. The client sends packets toward that address, and routers forward them along the network.
4. For HTTPS, the browser establishes encryption and verifies the server certificate for the name.
5. The browser uses the HTTP protocol to request the resource. The server replies with a status and the requested content when available.
6. The browser reads the response, retrieves any additional resources and displays the page.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Sanitized connectivity and DNS results](network-check.txt). Includes the example domain's public address records.

## 8. Commit details

`Check HTTPS and DNS and explain web communication`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-07-networking/README.md).
