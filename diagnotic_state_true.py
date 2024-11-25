# https://github.com/shipcod3/canTot/blob/main/modules/diagnostic_state.py
from sploitkit import *
from pyvit import can
from pyvit.hw import socketcan

class diagnostic_state(Module):
    """ This module will keep the vehicle in a diagnostic state on loop by sending tester present packet.   
    """

    # Configuration for the module, including interface and Arbitration ID (ARBID)
    config = Config({
        Option(
            'INTERFACE',                # Option for the CAN interface to use
            "CAN interface",            # Description for the interface option
            True,                       # Indicates this option is required
        ): str("vcan0"),                # Default value for the CAN interface
        Option(
            'ARBID',                    # Option for the Arbitration ID
            "Arbitration ID (Default: 0x7DF)",  # Description for the ARBID option
            True,                       # Indicates this option is required
        ): 0x7DF,                       # Default Arbitration ID for communication
    })    
    
    def run(self):
        # Initialize the CAN device using the specified interface
        dev = socketcan.SocketCanDev(self.config.option('INTERFACE').value)

        # Start the CAN device
        dev.start()
        print("[*] Putting the vehicle in a diagnostic state...")
        
        # Create a CAN frame with the specified Arbitration ID
        frame = can.Frame(self.config.option('ARBID').value)
        
        # Set the data for the frame to indicate a "tester present" signal
        frame.data = [0x01, 0x3E]
        
        print("Press Ctrl+C to stop or cancel")
        
        # Continuously send the "tester present" frame to keep the diagnostic state active
        while True:
            dev.send(frame)
        
        # Pass statement is redundant here but kept for structural completion
        pass