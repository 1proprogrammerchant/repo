from lilaclib import *

def pre_build():
  deps = [
    'hstspreload',
    'sniffio',
    'chardet',
    'idna',
    'rfc3986',
    'httpcore-latest',
    'charset-normalizer',
  ]
  pypi_pre_build(
    pypi_name = 'httpx',
    provides = ['python-httpx'],
    conflicts = ['python-httpx'],
    depends = [f'python-{x}' for x in deps],
    depends_setuptools = False,
    optdepends = [
      'python-brotlipy: decoding for "brotli" compressed responses',
      'python-urllib3: support for the httpx.URLLib3Transport class',
    ],
    prepare = '''\
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \\
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \\
      -i httpx/_config.py''',
  )

def post_build():
  pypi_post_build()
