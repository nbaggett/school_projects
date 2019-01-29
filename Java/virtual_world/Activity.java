public class Activity extends Action
{
    private ActiveEntity activeEntity;
;

    public Activity(ActiveEntity activeEntity, WorldModel world, ImageStore imageStore)
    {
        super(world, imageStore);
        this.activeEntity = activeEntity;
    }

    public void executeAction(EventScheduler scheduler)
    {
        activeEntity.executeActivity(super.getWorld(), super.getImageStore(), scheduler);
    }
}
