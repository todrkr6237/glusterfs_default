from distutils.core import setup

DESC = """GlusterFS is a clustered file-system capable of scaling to
several petabytes. It aggregates various storage bricks over Infiniband
RDMA or TCP/IP interconnect into one large parallel network file system.
GlusterFS is one of the most sophisticated file systems in terms of
features and extensibility.  It borrows a powerful concept called
Translators from GNU Hurd kernel. Much of the code in GlusterFS is in
user space and easily manageable.

This package contains the Python interface to the libgfapi library."""

setup(
    name='glusterfs-api',
    version='3.5.2',
    description='Python client library for the GlusterFS libgfapi',
    long_description=DESC,
    author='Gluster Community',
    author_email='gluster-devel@nongnu.org',
    license='LGPLv3',
    url='http://gluster.org/',
    package_dir={'gluster':''},
    packages=['gluster']
)
