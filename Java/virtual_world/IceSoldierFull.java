import processing.core.PImage;
import java.util.List;
import java.util.Optional;

public class IceSoldierFull extends AnimatedEntity
{
    private int minerCount;

    public IceSoldierFull(String id, Point position, List<PImage> images,int actionPeriod, int animationPeriod, int minerCount) {
        super(id, position, images, actionPeriod, animationPeriod);
        this.minerCount = minerCount;
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler) {
        Optional<Entity> icefort = Movable.findNearest(world, super.getPosition(), IceFort.class);

        if (icefort.isPresent() &&
                moveTo(scheduler, world, icefort.get())) {
            transform(world, scheduler, imageStore);
        } else {
            scheduler.scheduleEvent(this,
                    new Activity(this, world, imageStore),
                    super.getActionPeriod());
        }
    }
    private void transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore) {
        IceSoldierNotFull soldier = new IceSoldierNotFull(super.getId(), super.getPosition(), super.getImages(),
                super.getActionPeriod(), super.getAnimationPeriod(), minerCount);

        remove(world);
        scheduler.unscheduleAllEvents(this);

        world.addEntity(soldier);
        soldier.scheduleActions(scheduler, world, imageStore);
    }
}
