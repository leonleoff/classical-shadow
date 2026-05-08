from abc import ABC, abstractmethod

from qiskit import QuantumCircuit


class ShadowProtocol(ABC):

    def get_num_qubits(self) -> int:
        return len(self.get_state_circuit().qubits)

    @abstractmethod
    def get_state_circuit(self) -> QuantumCircuit:
        """ "Returns the quantum circuit that prepare the state of interest."""
        raise NotImplementedError("This method should be implemented by subclasses")

    @abstractmethod
    def run_circuit_and_get_measurement(self, circuit):
        raise NotImplementedError("This function is not yet implemented.")
