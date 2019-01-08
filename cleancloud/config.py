import collections
import os.path
import re
import settings
import utils

_CAMERA_CONFIG_FILE_NAME = 'thread-%(id)s.conf'

def get_camera(camera_id, as_lines=False):

    camera_config_path = os.path.join(settings.CONF_PATH, _CAMERA_CONFIG_FILE_NAME) % {'id': camera_id}

    print 'reading camera config from %(path)s...' % {'path': camera_config_path}

    try:
        f = open(camera_config_path, 'r')

    except Exception as e:
        logging.error('could not open camera config file: %(msg)s' % {'msg': unicode(e)})

        raise

    try:
        lines = [l.strip() for l in f.readlines()]

    except Exception as e:
        logging.error('could not read camera config file %(path)s: %(msg)s' % {
            'path': camera_config_path, 'msg': unicode(e)})

        raise

    finally:
        f.close()

    if as_lines:
        return lines

    camera_config = _conf_to_dict(lines,
                                  no_convert=['@name', '@network_share_name', '@network_smb_ver', '@network_server',
                                              '@network_username', '@network_password', '@storage_device',
                                              '@upload_server', '@upload_username', '@upload_password'])

    return camera_config


def _conf_to_dict(lines, list_names=None, no_convert=None):
    if list_names is None:
        list_names = []

    if no_convert is None:
        no_convert = []

    data = collections.OrderedDict()

    for line in lines:
        line = line.strip()
        if len(line) == 0:  # empty line
            continue

        match = re.match('^#\s*(@\w+)\s*(.*)', line)
        if match:
            name, value = match.groups()[:2]

        elif line.startswith('#') or line.startswith(';'):  # comment line
            continue

        else:
            parts = line.split(None, 1)
            if len(parts) == 1:  # empty value
                parts.append('')

            (name, value) = parts

            value = value.strip()

        if name in list_names:
            data.setdefault(name, []).append(value)

        else:
            data[name] = value

    return data
