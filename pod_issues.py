# Cheat Sheet for future Pod Issues, i.e. Pod not found

# Number one thing is to just kill the tunnel and kill Minikube, restart your computer.

"""
# Kubernetes Pod Troubleshooting Cheatsheet

# 1. Verify Pod Status
kubectl get pods -n <namespace>
kubectl describe pod <pod-name> -n <namespace>  # Check for errors in the "Events" section.

# 2. Verify Kubernetes Context
kubectl config current-context  # Ensure you’re in the correct cluster.
kubectl config use-context <context-name>  # Switch context if necessary.

# 3. Check Namespace
kubectl get namespaces  # List all namespaces.
kubectl get pods -n <namespace>  # List pods in a specific namespace.

# 4. Identify the Correct Pod
kubectl get pods -n <namespace>  # Always use the latest pod name.

# 5. Fix `NotFound` Errors
kubectl get pods -n <namespace>  # Ensure the pod exists.
minikube status  # Check Minikube health.
kubectl apply -f <yaml-file>  # Reapply YAML configurations.

# 6. Reapply YAML Configurations
kubectl apply -f <yaml-file>  # Apply configurations.
kubectl delete -f <yaml-file>  # Delete resources if needed.
kubectl apply -f <yaml-file>  # Reapply for a fresh start.

# 7. Test Pod Connectivity
kubectl exec -it <pod-name> -n <namespace> -- echo "Hello, world!"  # Run a simple command in the pod.

# 8. Copy Files to Pod
kubectl cp <local-file-path> <pod-name>:<destination-path> -n <namespace>  # Copy file to pod.
kubectl exec -it <pod-name> -n <namespace> -- ls <destination-path>  # Verify the file exists.

# 9. Check Logs
kubectl logs <pod-name> -n <namespace>  # Inspect pod logs for errors.

# 10. Restart Minikube Tunnel
pkill -f 'minikube tunnel'  # Kill the existing tunnel.
minikube tunnel  # Restart the tunnel.

# 11. Access the Flink Web UI
kubectl port-forward service/flink-jobmanager 8081:8081 -n <namespace>  # Forward Flink JobManager service port.
# Open the Web UI in your browser: http://localhost:8081

# 12. Cleanup Resources
kubectl delete -f <yaml-file>  # Delete existing resources.
kubectl apply -f <yaml-file>  # Reapply configurations.

# Common Commands Summary
# List pods in a namespace
kubectl get pods -n <namespace>

# Show details and events for a specific pod
kubectl describe pod <pod-name> -n <namespace>

# Show logs of a pod
kubectl logs <pod-name> -n <namespace>

# Execute a command in a pod
kubectl exec -it <pod-name> -n <namespace> -- <command>

# Copy a file to/from a pod
kubectl cp <src> <dest> -n <namespace>

# Apply or reapply a YAML configuration
kubectl apply -f <yaml-file>

# Delete resources defined in a YAML file
kubectl delete -f <yaml-file>

# Ensure Minikube network connectivity
minikube tunnel
    

Test:
kubectl exec -it flink-jobmanager-c59544b59-9f869 -- echo 'Hello, Flink!'


"""