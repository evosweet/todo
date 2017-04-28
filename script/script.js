Todo = function (data) {
    this.id = ko.observable(data.id);
    this.name = ko.observable(data.name);
    this.status = ko.observable(data.status);
};

var ViewModel = function () {
    self = this;
    self.toList = ko.observableArray([]);
    $.getJSON("http://localhost:8080/all", function (data) {
        // Now use this data to update your view models, 
        // and Knockout will update your UI automatically 
        self.toList(data);
    });
    done = function (task) {
        console.log(task);
    };
    undone = function (task) {
        console.log(task);
    };

    taskdel = function (task) {
        console.log(task);
        $.ajax({
            type: "POST",
            url: "http://localhost:8080/delTask",
            data: {'task_id':task.id},
            //success: success,
            //dataType: dataType
        });
        self.toList.remove(task);
    };

}

ko.applyBindings(new ViewModel());