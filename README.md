# Proxy Cache Server
Proxy caching allows a server to act as an intermediary between a user and a provider of web content. When a user accesses a website, proxies 
interpret and respond to requests on behalf of the original server.

# How Proxy Server Works
Proxies act as a gateway between the user and the source server, storing (or caching) the server’s resources. When the user attempts to access a resource, the proxy checks to see if it has a recent copy of the 
resource on hand. If so, the resource is immediately delivered to the user. If not, the resource is retrieved from the source and 
simultaneously cached to the proxy and delivered to the user.

<img src=https://www.cs.cornell.edu/courses/cs519/2003sp/homework/webproxy/webproxy.jpg>

# How Different are Proxy Cache Server and CDNs?
CDNs are geographically distributed networks of proxy servers and their objective is to serve content to users more quickly. Caching is the 
process of storing information for a set period of time on a computer. The main difference between CDNs and caching is while CDNs perform caching, not everything that performs caching is a CDN.
