🚀 Edge Constraints & Deployment Considerations

This project is designed with edge deployment constraints in mind, where compute, memory, and power are limited.
All Phase-1 design decisions prioritize feasibility, portability, and reliability over aggressive optimization.

📦 Model Size & Efficiency

A MobileNetV2 architecture is selected due to its lightweight design and strong suitability for edge inference.

The Phase-1 model uses a frozen backbone with a compact classification head, resulting in a small model footprint suitable for resource-constrained devices.

Why this matters:

🧠 Low parameter count

💾 Reduced memory footprint

⚡ Stable CPU-only inference

🧮 Compute & Memory Constraints

Edge devices typically operate with limited CPU capability and restricted RAM.

MobileNetV2 employs depthwise separable convolutions, which significantly reduce:

🔽 Computational complexity

🔽 Memory access overhead

when compared to standard convolutional neural networks, making it ideal for embedded workloads.

⏱️ Inference Latency Considerations

The model is optimized for inference rather than training, enabling efficient forward passes suitable for near real-time defect screening at the edge.

Phase-1 focuses on:

✅ Inference feasibility

✅ Architectural suitability for low-latency execution

⏳ Latency benchmarking and optimization are intentionally deferred to later phases.

🔄 Framework & Portability

To enable cross-platform deployment, the trained TensorFlow model is exported to the ONNX format.

ONNX allows inference using lightweight runtimes such as ONNX Runtime, enabling:

🔁 Framework-agnostic deployment

🌍 Portability across heterogeneous edge platforms

without dependency on a specific deep learning framework.

🔌 Offline Execution

The system supports fully offline inference, where all processing occurs locally on the device without cloud connectivity.

This is critical for industrial inspection systems requiring:

🕒 Deterministic latency

🛡️ High reliability

📍 Data locality

🛠️ Phase-2 Optimization Scope

Future work in Phase-2 includes edge-specific optimizations such as:

🔧 Model fine-tuning

📉 Post-training quantization

✂️ Pruning and operator-level optimization

These steps aim to further reduce inference latency and memory usage while preserving defect classification accuracy and recall.
