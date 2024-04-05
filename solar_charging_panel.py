import time

class SolarChargingPanel:
    def __init__(self, assigned_voltage):
        self.assigned_voltage = assigned_voltage
        self.is_charging = False

    def start_charging(self):
        self.is_charging = True
        print("Charging started.")

    def stop_charging(self):
        self.is_charging = False
        print("Charging stopped.")

    def monitor_voltage(self, current_voltage):
        if self.is_charging and current_voltage >= self.assigned_voltage:
            self.stop_charging()
        elif not self.is_charging and current_voltage < self.assigned_voltage:
            self.start_charging()

# Example usage:
if __name__ == "__main__":
    assigned_voltage = float(input("Enter the assigned voltage (V): "))
    panel = SolarChargingPanel(assigned_voltage)

    # Simulating voltage monitoring
    while True:
        current_voltage = float(input("Enter current voltage (V): "))
        panel.monitor_voltage(current_voltage)
        time.sleep(1)  # Simulating 1 second interval for voltage monitoring
