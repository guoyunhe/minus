import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import org.kde.kirigami 2.0 as Kirigami

Kirigami.ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Column {

        Text {
            text: 'Size: ' + task.size
        }

        Button {
            text: "Scan"
            onClicked: task.scan()
        }

        Button {
            text: "Exec"
            onClicked: task.exec()
        }
    }
}
