# SocketBridge

SocketBridge is a Python project that facilitates communication between devices over networks. It consists of two main scripts: `SocketLongDistance` and `SocketListener`.

---

## Getting Started

The project enables executing commands and transferring files between different devices. Below are the details of each script:

### SocketLongDistance

Used for executing commands on remote devices.

#### Features

- Remote command execution
- File download and upload

### SocketListener

Used for listening to commands and executing them on the local device.

#### Features

- Command listening
- File exchange

---

## Installation

To use SocketBridge, follow these steps:

1. **Download the latest version**:
   ```sh
   git clone https://github.com/LeatherFire/SocketBridge.git
   cd SocketBridge
   ```

2. **Switch to the tool's directory**:
   ```sh
   cd SocketBridge
   ```

3. **Run SocketBridge**:
   ```sh
   ./SocketLongDistance.py <IP_ADDRESS> <PORT>
   ```
   or
   ```sh
   ./SocketListener.py <IP_ADDRESS> <PORT>
   ```

---

## Usage

- For `SocketLongDistance`, specify the IP address and port of the remote device.
- For `SocketListener`, specify the IP address and port to listen on.

---

## Note

Remember to replace `<IP_ADDRESS>` and `<PORT>` with your own values.

---

## Contributing

Contributions are welcome! Feel free to open an issue for feedback and suggestions or submit a pull request directly.

---
