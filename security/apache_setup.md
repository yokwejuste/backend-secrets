To set up SSL for Apache, you can use the following configuration. This example assumes you have SSL certificates from Let's Encrypt, but it can be adapted for other certificate providers.

```apache
<VirtualHost *:443>
    ServerName yourdomain.com
    DocumentRoot /var/www/html

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem
    SSLCertificateChainFile /etc/letsencrypt/live/yourdomain.com/chain.pem

    # Recommended SSL Settings
    SSLProtocol all -SSLv2 -SSLv3
    SSLCipherSuite HIGH:!aNULL:!MD5
    SSLHonorCipherOrder on

    # Optional: Redirect HTTP to HTTPS
    <IfModule mod_rewrite.c>
        RewriteEngine On
        RewriteCond %{HTTPS} !=on
        RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R,L]
    </IfModule>

    # Proxy Settings (if needed to forward to an app server)
    ProxyPreserveHost On
    ProxyPass / http://localhost:8000/
    ProxyPassReverse / http://localhost:8000/
</VirtualHost>

# Redirect HTTP to HTTPS
<VirtualHost *:80>
    ServerName yourdomain.com
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
</VirtualHost>
```

### Explanation

- `ServerName`: Specifies the domain name.
- `SSLCertificateFile`, `SSLCertificateKeyFile`, and `SSLCertificateChainFile`: Paths to the SSL certificate files provided by Let's Encrypt or another certificate provider.
- `SSLProtocol` and `SSLCipherSuite`: Restricts SSL/TLS protocols and cipher suites for enhanced security.
- `ProxyPass` and `ProxyPassReverse`: Forwards requests to an application running on `http://localhost:8000`.
- The HTTP `VirtualHost` listens on port 80 and redirects all requests to HTTPS.

### Enable SSL and Restart Apache

1. Enable the SSL module:
   ```bash
   sudo a2enmod ssl
   ```
2. Enable proxy modules if using a proxy:
   ```bash
   sudo a2enmod proxy proxy_http rewrite
   ```
3. Restart Apache:
   ```bash
   sudo systemctl restart apache2
   ```

This configuration provides SSL termination with Apache, redirecting all HTTP traffic to HTTPS and forwarding requests to an application server running on port 8000 if needed.
