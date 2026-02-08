Edge Constraints & Deployment Considerations

This project is designed with edge deployment constraints in mind, where compute, memory, and power availability are limited. All architectural and framework decisions in Phase-1 prioritize feasibility and portability over experimental optimization.

Model Size & Efficiency

A MobileNetV2 architecture is selected due to its lightweight design and proven suitability for edge inference.
The Phase-1 model uses a frozen backbone with a shallow classification head, resulting in a compact model footprint that is suitable for deployment on resource-constrained devices.

Key benefits:

Low parameter count

Reduced memory footprint

Stable inference behavior on CPU-only systems

Compute & Memory Constraints

Edge devices typically operate with limited CPU capability and restricted RAM.
MobileNetV2 leverages depthwise separable convolutions, which significantly reduce:

Computational complexity

Memory access cost

compared to standard convolutional neural networks, making it appropriate for embedded inference workloads.

Inference Latency Considerations

The model is optimized for inference rather than training, enabling efficient forward passes suitable for near real-time defect screening at the edge.

Phase-1 focuses on:

Inference feasibility

Architectural suitability for low-latency execution

Latency optimization and benchmarking are intentionally deferred to later phases.

Framework & Portability

To enable cross-platform deployment, the trained TensorFlow model is exported to the ONNX format.
ONNX allows inference using lightweight runtimes such as ONNX Runtime, enabling portability across heterogeneous edge platforms without dependence on a specific deep learning framework.

Offline Execution

The system is designed to support fully offline inference, where all processing occurs locally on the device without cloud connectivity.
This is critical for industrial inspection systems that require:

Deterministic latency

High reliability

Data locality

Phase-2 Optimization Scope

Future work in Phase-2 includes edge-specific optimizations such as:

Model fine-tuning

Post-training quantization

Pruning and operator-level optimization

These steps aim to further reduce inference latency and memory usage while preserving defect classification accuracy and recall.
