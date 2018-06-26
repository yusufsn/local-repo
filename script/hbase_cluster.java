public ServerLoad getLoad(final ServerName sn) {
  return liveServers != null ? liveServers.get(sn) : null;
}

@InterfaceAudience.Private
public List<RegionState> getRegionsInTransition() {
  if (intransition == null) {
    return Collections.emptyList();
  }
  return Collections.unmodifiableList(intransition);
}

public String getClusterId() {
  return clusterId;
}