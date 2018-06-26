public ServerLoad getLoad(final ServerName sn) {
  ServerMetrics serverMetrics = metrics.getLiveServerMetrics().get(sn);
  return serverMetrics == null ? null : new ServerLoad(serverMetrics);
}

public String getClusterId() {
  return metrics.getClusterId();
}