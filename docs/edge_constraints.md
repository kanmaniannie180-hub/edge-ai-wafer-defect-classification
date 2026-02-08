Edge Constraints and Deployment Considerations

This project is designed with edge deployment constraints in mind, where computational resources, memory, and power consumption are limited.

Model Size and Efficiency

A lightweight MobileNetV2 architecture was selected to minimize model size while maintaining reasonable classification performance. The frozen-backbone Phase-1 model results in a compact footprint, making it suitable for deployment on resource-constrained edge devices.

Compute and Memory Constraints

Edge devices typically operate with limited CPU/GPU capability and restricted memory. The use of depthwise separable convolutions in MobileNetV2 significantly reduces computational complexity and memory usage compared to standard convolutional networks.

Inference Latency

The model is optimized for inference rather than training, enabling faster forward passes suitable for near real-time defect detection scenarios at the edge. Phase-1 focuses on inference feasibility rather than latency optimization.

Framework and Portability

To support cross-platform deployment, the trained TensorFlow model is exported to ONNX format, enabling inference using lightweight runtimes such as ONNX Runtime. This allows deployment across heterogeneous edge platforms without dependency on a specific deep learning framework.

Offline Execution

The system is designed to operate in offline environments, where inference is performed locally on the device without reliance on cloud connectivity. This is critical for industrial inspection systems with strict latency and reliability requirements.

Phase-2 Optimization Scope

Further edge-specific optimizations, including model fine-tuning, quantization, and pruning, are planned in Phase-2 to improve inference speed and reduce memory usage while maintaining defect recall.
