import processing.core.PImage;
import java.util.List;
import java.util.Optional;

public class IceSoldierNotFull extends AnimatedEntity
{
    private int minerCount;

    public IceSoldierNotFull(String id, Point position, List<PImage> images,int actionPeriod, int animationPeriod, int minerCount) {
        super(id, position, images, actionPeriod, animationPeriod);
        this.minerCount = minerCount;
    }

    public void incrementMinerCount()
    {
        minerCount++;
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler)
    {
        Optional<Entity> frozenminer = Movable.findNearest(world, super.getPosition(),
                FrozenMiner.class);

        if (!frozenminer.isPresent() ||
                !moveTo(scheduler, world, frozenminer.get()) ||
                !transform(world, scheduler, imageStore))
        {

            scheduler.scheduleEvent(this,
                    new Activity(this, world, imageStore),
                    super.getActionPeriod());
        }
    }

    private boolean transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore)
    {
        if (this.minerCount >= 1)
        {
            IceSoldierFull soldierFull = new IceSoldierFull(super.getId(), super.getPosition(), super.getImages(),
                    super.getActionPeriod(), super.getAnimationPeriod(), minerCount);

            this.remove(world);
            scheduler.unscheduleAllEvents(this);

            world.addEntity(soldierFull);
            soldierFull.scheduleActions(scheduler, world, imageStore);

            return true;
        }

        return false;
    }
}
