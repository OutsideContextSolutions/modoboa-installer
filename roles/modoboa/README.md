Deploy django using nginx, uwsgi, and postgres.
```yaml

- hosts: all
  vars:
    baseDomain: outsidecontext.solutions #/etc/letsencrypt/live/<first listed domain>/ is where letencrypt stores it's cert.
  roles:
   - role: uwsgiWebService
     user: newae
     plugin: python
     appname: server
     dbName: "{{ domain | replace('.','_') }}"
     dbUser: "{{ domain | replace('.','_') }}"
     dbConnection:
postgresql+psycopg2://{{dbUser}}:{{dbPasswordCommand.stdout}}@localhost:5432/{{dbName}}
     templates:
         - source: restapi/server/settings.template.py
           destination: restapi/server/settings.py
     repo: ssh://git@github.com/newaetech/autoanalysis.git
     module: server:app
     domain: newaeanalysis.outsidecontext.solutions
     requirements: restapi/requirements.txt
     chdir: /home/{{user}}/{{domain}}/restapi/server

```
