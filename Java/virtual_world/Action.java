public abstract class Action
{
    private WorldModel world;
    private ImageStore imageStore;

    public Action(WorldModel world, ImageStore imageStore)
    {
        this.world = world;
        this.imageStore = imageStore;
    }

    public WorldModel getWorld() { return world; }

    public ImageStore getImageStore() { return imageStore; }

    abstract void executeAction(EventScheduler scheduler);
}
