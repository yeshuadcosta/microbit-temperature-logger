input.onButtonPressed(Button.A, function () {
    basic.showString("" + input.temperature())
})
input.onButtonPressed(Button.AB, function () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.JumpUp), music.PlaybackMode.InBackground)
    while (true) {
        // 5 Second Interval
        actualtime = time * timeinterval
        datalogger.log(
        datalogger.createCV("Time", actualtime),
        datalogger.createCV("Temperature", input.temperature())
        )
        led.plotBarGraph(
        time,
        iterations
        )
        if (time == iterations) {
            terminate()
            break;
        }
        // Increment once after every iteration
        time += 1
        basic.pause(timeinterval * 1000)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + actualtime)
})
input.onGesture(Gesture.Shake, function () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Funeral), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Skull)
    datalogger.deleteLog(datalogger.DeleteType.Full)
})
// This function should be executed on time duration end
function terminate () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Ringtone), music.PlaybackMode.InBackground)
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Yes)
}
let actualtime = 0
let time = 0
let iterations = 0
let timeinterval = 0
datalogger.includeTimestamp(FlashLogTimeStampFormat.None)
music.setBuiltInSpeakerEnabled(true)
music.setVolume(200)
datalogger.setColumnTitles(
"Time",
"Temperature"
)
let duration = 300
timeinterval = 20
iterations = duration / timeinterval
time = 0
actualtime = 0
