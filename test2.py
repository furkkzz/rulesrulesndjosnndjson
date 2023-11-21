queries = [
    {
        "sigma_yaml_file": "appframework_django_exceptions.yml",
        "query": "\"SuspiciousOperation\" OR \"DisallowedHost\" OR \"DisallowedModelAdminLookup\" OR \"DisallowedModelAdminToField\" OR \"DisallowedRedirect\" OR \"InvalidSessionKey\" OR \"RequestDataTooBig\" OR \"SuspiciousFileOperation\" OR \"SuspiciousMultipartForm\" OR \"SuspiciousSession\" OR \"TooManyFieldsSent\" OR \"PermissionDenied\"",
    },
    {
        "sigma_yaml_file": "java_jndi_injection_exploitation_attempt.yml",
        "query": "\"com.sun.jndi.ldap.\" OR \"org.apache.logging.log4j.core.net.JndiManager\"",
    }
]