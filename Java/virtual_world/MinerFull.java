import processing.core.PImage;

import java.util.List;
import java.util.Optional;

public class MinerFull extends Miner
{
    private int resourceLimit;
    private int resourceCount;

    public MinerFull(String id, Point position, List<PImage> images, int resourceLimit,
                     int resourceCount, int actionPeriod, int animationPeriod) {
        super(id, position, images, actionPeriod, animationPeriod);
        this.resourceLimit = resourceLimit;
        this.resourceCount = resourceCount;
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler) {
        Optional<Entity> fullTarget = Movable.findNearest(world, super.getPosition(), Blacksmith.class);

        if (fullTarget.isPresent() &&
                moveTo(scheduler, world, fullTarget.get())) {
            transform(world, scheduler, imageStore);
        } else {
            scheduler.scheduleEvent(this,
                    new Activity(this, world, imageStore),
                    super.getActionPeriod());
        }
    }

    private void transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore) {
        MinerNotFull miner = new MinerNotFull(super.getId(), super.getPosition(), super.getImages(),
                this.resourceLimit, 0, super.getActionPeriod(), super.getAnimationPeriod());

        remove(world);
        scheduler.unscheduleAllEvents(this);

        world.addEntity(miner);
        miner.scheduleActions(scheduler, world, imageStore);
    }
}
