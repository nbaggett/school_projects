
public class Animation extends Action
{
    private AnimatedEntity animatedEntity;
    private int repeatCount;

    public Animation(AnimatedEntity animatedEntity, WorldModel world, ImageStore imageStore, int repeatCount)
    {
        super(world, imageStore);
        this.animatedEntity = animatedEntity;
        this.repeatCount = repeatCount;
    }

    public void executeAction(EventScheduler scheduler)
    {
        animatedEntity.nextImage();

        if (repeatCount != 1)
        {
            scheduler.scheduleEvent(animatedEntity,
                    new Animation(animatedEntity, super.getWorld(), super.getImageStore(), Math.max(repeatCount - 1, 0)),
                    animatedEntity.getAnimationPeriod());
        }
    }
}
