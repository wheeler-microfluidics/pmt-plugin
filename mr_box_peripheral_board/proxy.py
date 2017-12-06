from collections import OrderedDict
import time

from base_node_rpc.proxy import ConfigMixinBase
import pandas as pd

from .bin.upload import upload


try:
    # XXX The `node` module containing the `Proxy` class definition is
    # generated from the `mr_box_peripheral_board::Node` class in
    # the C++ file `src/Node.hpp`.
    from .node import (Proxy as _Proxy, I2cProxy as _I2cProxy,
                       SerialProxy as _SerialProxy)
    # XXX The `config` module containing the `Config` class definition is
    # generated from the Protocol Buffer file `src/config.proto`.
    from .config import Config


    class ConfigMixin(ConfigMixinBase):
        @property
        def config_class(self):
            return Config


    class ProxyMixin(ConfigMixin):
        '''
        Mixin class to add convenience wrappers around methods of the generated
        `node.Proxy` class.
        '''
        host_package_name = 'mr-box-peripheral-board'

        def get_adc_calibration(self):
            calibration_settings = \
            pd.Series(OrderedDict([('Self-Calibration_Gain', self.MAX11210_getSelfCalGain()),
                                   ('Self-Calibration_Offset', self.MAX11210_getSelfCalOffset()),
                                   ('System_Gain', self.MAX11210_getSysGainCal()),
                                   ('System_Offset', self.MAX11210_getSysOffsetCal())]))
            return calibration_settings



        def __init__(self, *args, **kwargs):
            super(ProxyMixin, self).__init__(*args, **kwargs)

        def close(self):
            self.terminate()

        @property
        def id(self):
            return self.config['id']

        @id.setter
        def id(self, id):
            return self.set_id(id)


    class Proxy(ProxyMixin, _Proxy):
        pass

    class I2cProxy(ProxyMixin, _I2cProxy):
        pass

    class SerialProxy(ProxyMixin, _SerialProxy):
        def __init__(self, *args, **kwargs):
            if not 'baudrate' in kwargs:
                kwargs['baudrate'] = 57600

            super(SerialProxy, self).__init__(*args, **kwargs)

        def flash_firmware(self):
            # currently, we're ignoring the hardware version, but eventually,
            # we will want to pass it to upload()
            self.terminate()
            upload()
            time.sleep(0.5)
            self._connect()


except (ImportError, TypeError):
    Proxy = None
    I2cProxy = None
    SerialProxy = None
