:source: bigip_profile_client_ssl.py

:orphan:

.. _bigip_profile_client_ssl_module:


bigip_profile_client_ssl - Manages client SSL profiles on a BIG-IP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Manages client SSL profiles on a BIG-IP.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                    <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <b>advertised_cert_authority</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies that the CAs that the system advertises to clients is being trusted by the profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>allow_expired_crl</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Instructs the system to use the specified CRL file even if it has expired.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>allow_non_ssl</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enables or disables acceptance of non-SSL connections.</div>
                                                    <div>When creating a new profile, the setting is provided by the parent profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cert_auth_depth</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the maximum number of certificates to be traversed in a client certificate chain.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cert_key_chain</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>One or more certificates and keys to associate with the SSL profile. This option is always a list. The keys in the list dictate the details of the client/key/chain combination. Note that BIG-IPs can only have one of each type of each certificate/key type. This means that you can only have one RSA, one DSA, and one ECDSA per profile. If you attempt to assign two RSA, DSA, or ECDSA certificate/key combo, the device will reject this.</div>
                                                    <div>This list is a complex list that specifies a number of keys.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>cert</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies a cert name for use.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>key</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Contains a key name.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>chain</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Contains a certificate chain that is relevant to the certificate and key mentioned earlier.</div>
                                                    <div>This key is optional.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>passphrase</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Contains the passphrase of the key file, should it require one.</div>
                                                    <div>Passphrases are encrypted on the remote BIG-IP device. Therefore, there is no way to compare them when updating a client SSL profile. Due to this, if you specify a passphrase, this module will always register a <code>changed</code> event.</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>ciphers</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>client_auth_crl</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the name of a file containing a list of revoked client certificates.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>client_auth_frequency</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>once</li>
                                                                                                                                                                                                <li>always</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the frequency of client authentication for an SSL session.</div>
                                                    <div>When <code>once</code>, specifies that the system authenticates the client once for an SSL session.</div>
                                                    <div>When <code>always</code>, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>client_certificate</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>ignore</li>
                                                                                                                                                                                                <li>require</li>
                                                                                                                                                                                                <li>request</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the way the system handles client certificates.</div>
                                                    <div>When <code>ignore</code>, specifies that the system ignores certificates from client systems.</div>
                                                    <div>When <code>require</code>, specifies that the system requires a client to present a valid certificate.</div>
                                                    <div>When <code>request</code>, specifies that the system requests a valid certificate from a client but always authenticate the client.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>name</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the name of the profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>options</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>netscape-reuse-cipher-change-bug</li>
                                                                                                                                                                                                <li>microsoft-big-sslv3-buffer</li>
                                                                                                                                                                                                <li>msie-sslv2-rsa-padding</li>
                                                                                                                                                                                                <li>ssleay-080-client-dh-bug</li>
                                                                                                                                                                                                <li>tls-d5-bug</li>
                                                                                                                                                                                                <li>tls-block-padding-bug</li>
                                                                                                                                                                                                <li>dont-insert-empty-fragments</li>
                                                                                                                                                                                                <li>no-ssl</li>
                                                                                                                                                                                                <li>no-dtls</li>
                                                                                                                                                                                                <li>no-session-resumption-on-renegotiation</li>
                                                                                                                                                                                                <li>no-tlsv1.1</li>
                                                                                                                                                                                                <li>no-tlsv1.2</li>
                                                                                                                                                                                                <li>no-tlsv1.3</li>
                                                                                                                                                                                                <li>single-dh-use</li>
                                                                                                                                                                                                <li>ephemeral-rsa</li>
                                                                                                                                                                                                <li>cipher-server-preference</li>
                                                                                                                                                                                                <li>tls-rollback-bug</li>
                                                                                                                                                                                                <li>no-sslv2</li>
                                                                                                                                                                                                <li>no-sslv3</li>
                                                                                                                                                                                                <li>no-tls</li>
                                                                                                                                                                                                <li>no-tlsv1</li>
                                                                                                                                                                                                <li>pkcs1-check-1</li>
                                                                                                                                                                                                <li>pkcs1-check-2</li>
                                                                                                                                                                                                <li>netscape-ca-dn-bug</li>
                                                                                                                                                                                                <li>netscape-demo-cipher-change-bug</li>
                                                                                                                                                                                                <li>none</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Options that the system uses for SSL processing in the form of a list. When creating a new profile, the list is provided by the parent profile.</div>
                                                    <div>When a <code>&#x27;&#x27;</code> or <code>none</code> value is provided all options for SSL processing are disabled.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>parent</b>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/Common/clientssl</div>
                                    </td>
                                                                <td>
                                                                        <div>The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the <code>clientssl</code> parent on the <code>Common</code> partition.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>partition</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Common</div>
                                    </td>
                                                                <td>
                                                                        <div>Device partition to manage resources on.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A dict object containing connection details.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>password</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The password for the user account used to connect to the BIG-IP.</div>
                                                    <div>You may omit this option by setting the environment variable <code>F5_PASSWORD</code>.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: pass, pwd</div>
                                    </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>server</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The BIG-IP host.</div>
                                                    <div>You may omit this option by setting the environment variable <code>F5_SERVER</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>server_port</b>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">443</div>
                                    </td>
                                                                <td>
                                                                        <div>The BIG-IP server port.</div>
                                                    <div>You may omit this option by setting the environment variable <code>F5_SERVER_PORT</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>user</b>
                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The username to connect to the BIG-IP with. This user must have administrative privileges on the device.</div>
                                                    <div>You may omit this option by setting the environment variable <code>F5_USER</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>validate_certs</b>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>If <code>no</code>, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.</div>
                                                    <div>You may omit this option by setting the environment variable <code>F5_VALIDATE_CERTS</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>timeout</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>ssh_keyfile</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for <em>cli</em> transports.</div>
                                                    <div>You may omit this option by setting the environment variable <code>ANSIBLE_NET_SSH_KEYFILE</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>transport</b>
                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>cli</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>rest</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Configures the transport connection to use when connecting to the remote device.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>auth_provider</b>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Configures the auth provider for to obtain authentication tokens from the remote device.</div>
                                                    <div>This option is really used when working with BIG-IQ devices.</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>renegotiation</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enables or disables SSL renegotiation.</div>
                                                    <div>When creating a new profile, the setting is provided by the parent profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>retain_certificate</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>When <code>yes</code>, client certificate is retained in SSL session.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>secure_renegotiation</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>require</li>
                                                                                                                                                                                                <li>require-strict</li>
                                                                                                                                                                                                <li>request</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.</div>
                                                    <div>When <code>request</code> is set the system request secure renegotation of SSL connections.</div>
                                                    <div><code>require</code> is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.</div>
                                                    <div>The <code>require-strict</code> setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>server_name</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.</div>
                                                    <div>The server name can also be a wildcard string containing the asterisk <code>*</code> character.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sni_default</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.</div>
                                                    <div>When creating a new profile, the setting is provided by the parent profile.</div>
                                                    <div>There can be only one SSL profile with this setting enabled.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sni_require</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Requires that the network peers also provide SNI support, this setting only takes effect when <code>sni_default</code> is set to <code>true</code>.</div>
                                                    <div>When creating a new profile, the setting is provided by the parent profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>state</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>When <code>present</code>, ensures that the profile exists.</div>
                                                    <div>When <code>absent</code>, ensures the profile is removed.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>strict_resume</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enables or disables the resumption of SSL sessions after an unclean shutdown.</div>
                                                    <div>When creating a new profile, the setting is provided by the parent profile.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>trusted_cert_authority</b>
                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.8)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Specifies a client CA that the system trusts.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Requires BIG-IP software version >= 12
    - For more information on using Ansible to manage F5 Networks devices see https://www.ansible.com/integrations/networks/f5.
    - Requires BIG-IP software version >= 12.
    - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the :ref:`bigip_config <bigip_config_module>` module to save the running configuration. Refer to the module's documentation for the correct usage of the module to save your running configuration.


Examples
--------

.. code-block:: yaml

    
    - name: Create client SSL profile
      bigip_profile_client_ssl:
        state: present
        name: my_profile
        provider:
          server: lb.mydomain.com
          user: admin
          password: secret
      delegate_to: localhost

    - name: Create client SSL profile with specific ciphers
      bigip_profile_client_ssl:
        state: present
        name: my_profile
        ciphers: "!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA"
        provider:
          server: lb.mydomain.com
          user: admin
          password: secret
      delegate_to: localhost

    - name: Create client SSL profile with specific SSL options
      bigip_profile_client_ssl:
        state: present
        name: my_profile
        options:
          - no-sslv2
          - no-sslv3
        provider:
          server: lb.mydomain.com
          user: admin
          password: secret
      delegate_to: localhost

    - name: Create client SSL profile require secure renegotiation
      bigip_profile_client_ssl:
        state: present
        name: my_profile
        secure_renegotiation: request
        provider:
          server: lb.mydomain.com
          user: admin
          password: secret
      delegate_to: localhost

    - name: Create a client SSL profile with a cert/key/chain setting
      bigip_profile_client_ssl:
        state: present
        name: my_profile
        cert_key_chain:
          - cert: bigip_ssl_cert1
            key: bigip_ssl_key1
            chain: bigip_ssl_cert1
        provider:
          server: lb.mydomain.com
          user: admin
          password: secret
      delegate_to: localhost




Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
                                                                                                                                                                                                                        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>allow_non_ssl</b>
                    <br/><div style="font-size: small; color: red">bool</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>Acceptance of non-SSL connections.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>ciphers</b>
                    <br/><div style="font-size: small; color: red">str</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>The ciphers applied to the profile.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">!SSLv3:!SSLv2:ECDHE+AES-GCM+SHA256:ECDHE-RSA-AES128-CBC-SHA</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>options</b>
                    <br/><div style="font-size: small; color: red">list</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>The list of options for SSL processing.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;no-sslv2&#x27;, &#x27;no-sslv3&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>renegotiation</b>
                    <br/><div style="font-size: small; color: red">bool</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>Renegotiation of SSL sessions.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>secure_renegotiation</b>
                    <br/><div style="font-size: small; color: red">str</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>The method of secure SSL renegotiation.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">request</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>strict_resume</b>
                    <br/><div style="font-size: small; color: red">bool</div>
                </td>
                <td>changed</td>
                <td>
                                            <div>Resumption of SSL sessions after an unclean shutdown.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------



This module is **preview** which means that it is not guaranteed to have a backwards compatible interface.




Author
~~~~~~

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

