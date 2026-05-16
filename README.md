# Velero-AKS-Testing

## Overview

This project provides a reference implementation and testing environment for [Velero](https://velero.io/), an open-source backup and disaster recovery tool for Kubernetes clusters, specifically targeting Azure Kubernetes Service (AKS). It demonstrates how to back up and restore workloads, persistent volumes, and cluster resources in AKS using Velero.

## Features

- **Backup and Restore**: Protects AKS workloads and persistent data using Velero.
- **Sample Web App**: Includes a simple Flask web application that stores visit counts on a Persistent Volume, demonstrating stateful backup/restore.
- **Azure Integration**: Uses Azure Blob Storage for backup storage and supports Azure authentication.
- **Disaster Recovery**: Provides scripts and configuration for simulating and recovering from failures.

## Project Structure

- `app.py` — Sample Flask web app for AKS, demonstrates persistent storage.
- `app.yaml` — Kubernetes manifests for deploying the sample app, PersistentVolumeClaim, and ConfigMap.
- `Dockerfile` — Multi-stage Dockerfile for building Velero and the sample app.
- `Makefile` — Build and deployment automation for Velero.
- `go.mod`, `go.sum` — Go module files for Velero dependencies.
- `credentials-velero`, `credentials-velero-secondary` — Azure credentials for Velero to access storage and resources (do not commit real secrets!).
- `velero` — Velero binary (not human-readable).
- `netlify.toml` — Netlify configuration (if using static site deployment for docs).

## Prerequisites

- Azure subscription with AKS and Blob Storage access
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Velero CLI](https://velero.io/docs/)
- Docker
- Go (for building Velero)

## Quick Start

1. **Clone the repository**

   ```sh
   git clone https://github.com/Simar0024/Velero-AKS-Testing.git
   cd Velero-AKS-Testing
   ```

2. **Build and Deploy the Sample App**

   ```sh
   kubectl apply -f app.yaml
   # Build and push Docker image if needed
   ```

3. **Configure Velero**

   - Set up Azure credentials in `credentials-velero` and/or `credentials-velero-secondary`.
   - Install Velero with Azure plugin:

     ```sh
     velero install \
       --provider azure \
       --plugins velero/velero-plugin-for-microsoft-azure:v1.8.0 \
       --bucket <BUCKET> \
       --secret-file ./credentials-velero \
       --backup-location-config resourceGroup=<RESOURCE_GROUP>,storageAccount=<STORAGE_ACCOUNT>,subscriptionId=<SUBSCRIPTION_ID>
     ```

4. **Perform Backups**

   ```sh
   velero backup create app-backup --include-namespaces app-ns
   ```

5. **Restore from Backup**

   ```sh
   velero restore create --from-backup app-backup
   ```

## Security Notice

- **Never commit real Azure credentials to version control.**
- Use sample or dummy values in `credentials-velero*` files for demonstration only.

## References

- [Velero Documentation](https://velero.io/docs/)
- [AKS Documentation](https://docs.microsoft.com/en-us/azure/aks/)

## License

Apache 2.0. See [LICENSE](LICENSE) for details.
